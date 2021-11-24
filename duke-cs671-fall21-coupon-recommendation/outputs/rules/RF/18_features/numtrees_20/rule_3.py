def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[6]>1:
		# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.8631, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Coupon", "instances": 29, "metric_value": 0.7355, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Time", "instances": 20, "metric_value": 0.8813, "depth": 4}
				if obj[2]>0:
					# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[16]<=0:
						# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[17]>1:
							# {"feature": "Children", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[8]>0:
								# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[5]>0:
									# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]>0:
											return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]<=0:
									# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[10]>2:
										return 'True'
									elif obj[10]<=2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[8]<=0:
								return 'False'
							else: return 'False'
						elif obj[17]<=1:
							return 'True'
						else: return 'True'
					elif obj[16]>0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]>3:
				return 'False'
			else: return 'False'
		elif obj[13]>2.0:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[3]>2:
				return 'True'
			elif obj[3]<=2:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[9]<=2:
					return 'False'
				elif obj[9]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=1:
		# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[14]<=3.0:
			# {"feature": "Time", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Income", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[11]>2:
					return 'True'
				elif obj[11]<=2:
					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[14]>3.0:
			return 'False'
		else: return 'False'
	else: return 'True'
