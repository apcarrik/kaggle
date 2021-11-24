def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Gender", "instances": 41, "metric_value": 0.9012, "depth": 1}
	if obj[7]<=0:
		# {"feature": "Passanger", "instances": 21, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[11]>0:
				# {"feature": "Temperature", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]<=55:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=3:
						return 'True'
					elif obj[5]>3:
						return 'False'
					else: return 'False'
				elif obj[3]>55:
					return 'False'
				else: return 'False'
			elif obj[11]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[7]>0:
		# {"feature": "Carryaway", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[16]<=3.0:
			# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[17]>1.0:
				# {"feature": "Bar", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[14]>0.0:
					# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Temperature", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[3]<=55:
							# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[8]<=1:
								return 'True'
							elif obj[8]>1:
								return 'False'
							else: return 'False'
						elif obj[3]>55:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[14]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[17]<=1.0:
				return 'True'
			else: return 'True'
		elif obj[16]>3.0:
			return 'True'
		else: return 'True'
	else: return 'False'
