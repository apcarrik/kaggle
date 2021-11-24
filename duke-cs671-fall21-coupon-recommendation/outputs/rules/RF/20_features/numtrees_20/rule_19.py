def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Income", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[13]>2:
		# {"feature": "Weather", "instances": 35, "metric_value": 0.8224, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Coupon_validity", "instances": 29, "metric_value": 0.6632, "depth": 3}
			if obj[6]>0:
				# {"feature": "Gender", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[7]>0:
					# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[11]>0:
						# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[8]<=3:
							# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[3]>55:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[15]>0.0:
									return 'False'
								elif obj[15]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=55:
								return 'True'
							else: return 'True'
						elif obj[8]>3:
							return 'False'
						else: return 'False'
					elif obj[11]<=0:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>1:
			# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[15]<=2.0:
				return 'False'
			elif obj[15]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[13]<=2:
		# {"feature": "Time", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[4]>1:
			return 'False'
		elif obj[4]<=1:
			# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[16]>2.0:
				# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[14]<=2.0:
					return 'True'
				elif obj[14]>2.0:
					return 'False'
				else: return 'False'
			elif obj[16]<=2.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
