def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Occupation", "instances": 41, "metric_value": 0.9892, "depth": 1}
	if obj[12]<=14:
		# {"feature": "Time", "instances": 38, "metric_value": 0.998, "depth": 2}
		if obj[4]>0:
			# {"feature": "Bar", "instances": 30, "metric_value": 0.971, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Income", "instances": 27, "metric_value": 0.9183, "depth": 4}
				if obj[13]>2:
					# {"feature": "Driving_to", "instances": 21, "metric_value": 0.7919, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Age", "instances": 19, "metric_value": 0.6292, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[15]>1.0:
								# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[5]<=3:
									# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[2]<=0:
										return 'False'
									elif obj[2]>0:
										return 'True'
									else: return 'True'
								elif obj[5]>3:
									return 'True'
								else: return 'True'
							elif obj[15]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[8]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[13]<=2:
					# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=0:
						return 'True'
					elif obj[7]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[14]>2.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[17]<=2.0:
				return 'True'
			elif obj[17]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[12]>14:
		return 'False'
	else: return 'False'
