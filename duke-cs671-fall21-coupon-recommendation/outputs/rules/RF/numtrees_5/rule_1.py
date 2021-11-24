def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Driving_to", "instances": 204, "metric_value": 0.9526, "depth": 1}
	if obj[0]>0:
		# {"feature": "Coupon_validity", "instances": 104, "metric_value": 1.0, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Occupation", "instances": 59, "metric_value": 0.9529, "depth": 3}
			if obj[12]<=10:
				# {"feature": "Coupon", "instances": 40, "metric_value": 0.9982, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[15]<=1.0:
						# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[14]>0.0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[14]<=0.0:
							# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[9]<=1:
								return 'False'
							elif obj[9]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[15]>1.0:
						# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[11]>0:
							return 'False'
						elif obj[11]<=0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[5]>2:
					# {"feature": "Maritalstatus", "instances": 18, "metric_value": 0.8524, "depth": 5}
					if obj[9]<=0:
						# {"feature": "Weather", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[13]>1:
								return 'False'
							elif obj[13]<=1:
								return 'True'
							else: return 'True'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					elif obj[9]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[12]>10:
				# {"feature": "Carryaway", "instances": 19, "metric_value": 0.6292, "depth": 4}
				if obj[16]<=3.0:
					# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[15]>-1.0:
						return 'True'
					elif obj[15]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[16]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Coupon", "instances": 45, "metric_value": 0.9183, "depth": 3}
			if obj[5]>1:
				# {"feature": "Maritalstatus", "instances": 39, "metric_value": 0.9612, "depth": 4}
				if obj[9]<=2:
					# {"feature": "Gender", "instances": 37, "metric_value": 0.9353, "depth": 5}
					if obj[7]>0:
						# {"feature": "Occupation", "instances": 22, "metric_value": 0.7732, "depth": 6}
						if obj[12]>2:
							# {"feature": "Income", "instances": 16, "metric_value": 0.3373, "depth": 7}
							if obj[13]>1:
								return 'False'
							elif obj[13]<=1:
								# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=55:
									return 'False'
								elif obj[3]>55:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]<=2:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4]>0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=0:
									return 'False'
								elif obj[11]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]<=0:
						# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[12]>1:
							# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[15]<=0.0:
								# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[8]>1:
										return 'False'
									elif obj[8]<=1:
										# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2]>0:
											return 'True'
										elif obj[2]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]>0:
									return 'True'
								else: return 'True'
							elif obj[15]>0.0:
								return 'True'
							else: return 'True'
						elif obj[12]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>2:
					return 'True'
				else: return 'True'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Coupon", "instances": 100, "metric_value": 0.795, "depth": 2}
		if obj[5]>0:
			# {"feature": "Income", "instances": 85, "metric_value": 0.7219, "depth": 3}
			if obj[13]>0:
				# {"feature": "Occupation", "instances": 72, "metric_value": 0.6167, "depth": 4}
				if obj[12]>2.598727523643797:
					# {"feature": "Education", "instances": 58, "metric_value": 0.4798, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Time", "instances": 40, "metric_value": 0.6098, "depth": 6}
						if obj[4]<=3:
							# {"feature": "Restaurantlessthan20", "instances": 29, "metric_value": 0.7355, "depth": 7}
							if obj[17]>1.0:
								# {"feature": "Temperature", "instances": 26, "metric_value": 0.6194, "depth": 8}
								if obj[3]<=55:
									# {"feature": "Weather", "instances": 15, "metric_value": 0.8366, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[1]>0:
											# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[8]<=4:
												# {"feature": "Children", "instances": 9, "metric_value": 0.7642, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[14]>1.0:
														return 'False'
													elif obj[14]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[8]>4:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[2]>1:
										return 'True'
									else: return 'True'
								elif obj[3]>55:
									return 'True'
								else: return 'True'
							elif obj[17]<=1.0:
								# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=2:
									return 'False'
								elif obj[8]>2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>3:
							return 'True'
						else: return 'True'
					elif obj[11]>2:
						return 'True'
					else: return 'True'
				elif obj[12]<=2.598727523643797:
					# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[15]<=3.0:
						# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[11]>0:
									return 'True'
								elif obj[11]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[15]>3.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[13]<=0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[12]<=7:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=2:
							return 'True'
						elif obj[4]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]>7:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]<=0:
			# {"feature": "Bar", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=3:
						return 'True'
					elif obj[8]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[14]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
