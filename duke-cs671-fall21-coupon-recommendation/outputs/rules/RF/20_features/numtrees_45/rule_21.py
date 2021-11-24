def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[14]<=1.0:
		# {"feature": "Age", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[8]<=6:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[5]<=2:
				return 'False'
			elif obj[5]>2:
				# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[7]>0:
					# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]>0:
						return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>6:
			return 'True'
		else: return 'True'
	elif obj[14]>1.0:
		# {"feature": "Temperature", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[3]>55:
			return 'True'
		elif obj[3]<=55:
			return 'False'
		else: return 'False'
	else: return 'True'
