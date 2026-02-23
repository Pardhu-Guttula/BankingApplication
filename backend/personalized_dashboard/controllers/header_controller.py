# Epic Title: Design and Implement Header for the E-commerce Platform

from flask import Blueprint, render_template

header_bp = Blueprint('header', __name__)

@header_bp.route('/header')
def header():
    return render_template('header.html')