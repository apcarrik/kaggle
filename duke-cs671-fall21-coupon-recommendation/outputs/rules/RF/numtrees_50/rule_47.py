def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Driving_to", "instances": 20, "metric_value": 1.0, "depth": 1}
	if obj[0]>0:
		# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[14]<=2.0:
			# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[8]<=4:
				return 'False'
			elif obj[8]>4:
				# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=55:
					return 'False'
				elif obj[3]>55:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[14]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[9]<=1:
			return 'True'
		elif obj[9]>1:
			return 'False'
		else: return 'False'
	else: return 'True'
