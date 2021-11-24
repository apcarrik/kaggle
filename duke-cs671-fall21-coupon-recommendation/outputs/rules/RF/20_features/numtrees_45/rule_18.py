def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[11]>0:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[5]>2:
			# {"feature": "Temperature", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[3]>55:
				# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0:
					return 'False'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=55:
				return 'True'
			else: return 'True'
		elif obj[5]<=2:
			return 'False'
		else: return 'False'
	elif obj[11]<=0:
		# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[17]>0.0:
			return 'True'
		elif obj[17]<=0.0:
			# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=0:
				return 'False'
			elif obj[0]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
