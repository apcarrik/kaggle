def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Temperature", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[2]>55:
		# {"feature": "Age", "instances": 72, "metric_value": 0.9544, "depth": 2}
		if obj[7]<=5:
			# {"feature": "Direction_same", "instances": 61, "metric_value": 0.9842, "depth": 3}
			if obj[17]<=0:
				# {"feature": "Coupon_validity", "instances": 52, "metric_value": 0.9989, "depth": 4}
				if obj[5]>0:
					# {"feature": "Bar", "instances": 27, "metric_value": 0.9751, "depth": 5}
					if obj[13]<=0.0:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[10]<=2:
							# {"feature": "Distance", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[18]>1:
								# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[3]>0:
									# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[4]>2:
										# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[15]<=2.0:
											return 'True'
										elif obj[15]>2.0:
											return 'False'
										else: return 'False'
									elif obj[4]<=2:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[18]<=1:
								return 'False'
							else: return 'False'
						elif obj[10]>2:
							return 'True'
						else: return 'True'
					elif obj[13]>0.0:
						# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[8]<=1:
							# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[11]>0:
									return 'False'
								elif obj[11]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>3:
								return 'True'
							else: return 'True'
						elif obj[8]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Occupation", "instances": 25, "metric_value": 0.9427, "depth": 5}
					if obj[11]>2:
						# {"feature": "Distance", "instances": 20, "metric_value": 0.9928, "depth": 6}
						if obj[18]>1:
							# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[15]>1.0:
								# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[12]<=4:
									return 'True'
								elif obj[12]>4:
									return 'False'
								else: return 'False'
							elif obj[15]<=1.0:
								# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=0:
									return 'False'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[18]<=1:
							# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[10]>0:
								return 'False'
							elif obj[10]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]<=2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[17]>0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[11]<=11:
					return 'True'
				elif obj[11]>11:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]>5:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[11]>1:
				return 'True'
			elif obj[11]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=55:
		# {"feature": "Distance", "instances": 55, "metric_value": 0.9806, "depth": 2}
		if obj[18]>1:
			# {"feature": "Age", "instances": 37, "metric_value": 0.9995, "depth": 3}
			if obj[7]<=4:
				# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9576, "depth": 4}
				if obj[16]>0.0:
					# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.995, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[0]>0:
							# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[11]<=17:
								# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[10]>0:
									return 'True'
								elif obj[10]<=0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]>1:
										return 'True'
									elif obj[3]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[11]>17:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]>2:
									return 'False'
								elif obj[3]<=2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>0:
						# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[10]<=2:
							# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[8]<=0:
								return 'False'
							elif obj[8]>0:
								# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[10]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[16]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[7]>4:
				# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[18]<=1:
			# {"feature": "Age", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[7]<=5:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[4]>1:
					# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[12]>1:
							return 'True'
						elif obj[12]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[7]>5:
				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'False'
