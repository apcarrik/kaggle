def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon_validity", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[6]>0:
		# {"feature": "Restaurantlessthan20", "instances": 44, "metric_value": 0.976, "depth": 2}
		if obj[16]>1.0:
			# {"feature": "Education", "instances": 38, "metric_value": 0.998, "depth": 3}
			if obj[11]<=3:
				# {"feature": "Weather", "instances": 35, "metric_value": 0.9852, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Occupation", "instances": 32, "metric_value": 0.9972, "depth": 5}
					if obj[12]<=17:
						# {"feature": "Time", "instances": 26, "metric_value": 0.9612, "depth": 6}
						if obj[4]>1:
							# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[1]>1:
								# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[15]<=1.0:
									# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[5]<=3:
										return 'True'
									elif obj[5]>3:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>0:
											return 'True'
										elif obj[7]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[15]>1.0:
									return 'False'
								else: return 'False'
							elif obj[1]<=1:
								return 'True'
							else: return 'True'
						elif obj[4]<=1:
							# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[8]>1:
								return 'False'
							elif obj[8]<=1:
								# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[3]>55:
									return 'True'
								elif obj[3]<=55:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[12]>17:
						# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[10]>0:
							return 'True'
						elif obj[10]<=0:
							# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[2]>1:
					return 'False'
				else: return 'False'
			elif obj[11]>3:
				return 'True'
			else: return 'True'
		elif obj[16]<=1.0:
			return 'False'
		else: return 'False'
	elif obj[6]<=0:
		# {"feature": "Temperature", "instances": 41, "metric_value": 0.8015, "depth": 2}
		if obj[3]<=55:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.4395, "depth": 3}
			if obj[12]<=20:
				# {"feature": "Age", "instances": 21, "metric_value": 0.2762, "depth": 4}
				if obj[8]<=5:
					return 'True'
				elif obj[8]>5:
					# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=0:
						return 'True'
					elif obj[0]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]>20:
				return 'False'
			else: return 'False'
		elif obj[3]>55:
			# {"feature": "Time", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[12]<=11:
					# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[11]<=2:
						return 'True'
					elif obj[11]>2:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[8]<=6:
							return 'False'
						elif obj[8]>6:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]>11:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2:
				# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'True'
