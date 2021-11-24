def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[5]>0:
		# {"feature": "Coupon_validity", "instances": 44, "metric_value": 0.9024, "depth": 2}
		if obj[6]>0:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[12]<=9:
				# {"feature": "Driving_to", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[7]>0:
						return 'False'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[12]>9:
				# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]<=0:
			# {"feature": "Bar", "instances": 20, "metric_value": 0.2864, "depth": 3}
			if obj[14]<=1.0:
				return 'True'
			elif obj[14]>1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=0:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
