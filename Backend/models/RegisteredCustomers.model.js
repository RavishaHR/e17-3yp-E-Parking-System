const mongoose = require('mongoose');
const uniqueValidator = require('mongoose-unique-validator');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const Schema = mongoose.Schema;

const RegisteredCustomersSchema = new Schema({
    name:{type: String, unique:true, required: false},
    email:{type: String, unique:true, required: true, match: [/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/]},
    contactnumber:{type: Number, required: false},
    password:{type: String, unique:true, required: true, minlength: 6, select: false },
    paymentmethod:{type: String, required: false},
    vehiclenumber:{type: [String], unique:false, required: false},
    vehiclemodel:{type: [String], unique:false, required: false},
    resetPasswordToken: String,
    resetPasswordExpire: Date
});

RegisteredCustomersSchema.pre("save", async function (next) {
    console.log("ismodified state");
    if(!this.isModified("password")){
        next();
    }
    const salt = await bcrypt.genSalt(10);
    this.password = await bcrypt.hash(this.password, salt)
    console.log(this.password);
    next();
});

RegisteredCustomersSchema.methods.matchPasswords = async function(password){
    const val = await bcrypt.compare(password, this.password);
    return val
};

RegisteredCustomersSchema.methods.getSignedToken = function(){
    return jwt.sign({ id: this._id }, process.env.JWT_SECRET, {expiresIn: process.env.JWT_EXPIRE});
};


RegisteredCustomersSchema.plugin(uniqueValidator, {message: 'Email already exists'});
const RegUser = mongoose.model("RegUser", RegisteredCustomersSchema);
module.exports = RegUser;