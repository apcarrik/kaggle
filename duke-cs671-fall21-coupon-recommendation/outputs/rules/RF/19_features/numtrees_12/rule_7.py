def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[18]<=2:
		# {"feature": "Age", "instances": 68, "metric_value": 0.9597, "depth": 2}
		if obj[7]>1:
			# {"feature": "Coupon", "instances": 49, "metric_value": 0.9973, "depth": 3}
			if obj[4]>1:
				# {"feature": "Income", "instances": 38, "metric_value": 0.9678, "depth": 4}
				if obj[12]<=7:
					# {"feature": "Children", "instances": 32, "metric_value": 0.9972, "depth": 5}
					if obj[9]>0:
						# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[16]>1.0:
							# {"feature": "Weather", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[14]<=3.0:
									return 'True'
								elif obj[14]>3.0:
									return 'False'
								else: return 'False'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						elif obj[16]<=1.0:
							# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[10]<=3:
									# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[11]>2:
										return 'False'
									elif obj[11]<=2:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]>2:
											return 'False'
										elif obj[3]<=2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[10]>3:
									return 'True'
								else: return 'True'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]<=0:
						# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[3]<=1:
							return 'False'
						elif obj[3]>1:
							# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[2]<=55:
								return 'True'
							elif obj[2]>55:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[12]>7:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Gender", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[6]>0:
					return 'False'
				elif obj[6]<=0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]>0:
							return 'False'
						elif obj[8]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]<=1:
			# {"feature": "Income", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[12]<=4:
				# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[10]>0:
					# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[3]>1:
						# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]<=1:
							return 'True'
						elif obj[8]>1:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				elif obj[10]<=0:
					return 'True'
				else: return 'True'
			elif obj[12]>4:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[18]>2:
		# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[8]<=0:
			return 'False'
		elif obj[8]>0:
			# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[7]<=2:
				return 'True'
			elif obj[7]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
