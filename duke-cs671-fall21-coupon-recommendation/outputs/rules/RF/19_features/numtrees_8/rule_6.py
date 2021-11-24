def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[0]>0:
		# {"feature": "Time", "instances": 117, "metric_value": 0.9974, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Direction_same", "instances": 62, "metric_value": 0.9383, "depth": 3}
			if obj[17]<=0:
				# {"feature": "Education", "instances": 42, "metric_value": 0.7919, "depth": 4}
				if obj[10]>1:
					# {"feature": "Coupon", "instances": 25, "metric_value": 0.9427, "depth": 5}
					if obj[4]>3:
						# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 7}
							if obj[11]>0:
								return 'False'
							elif obj[11]<=0:
								return 'True'
							else: return 'True'
						elif obj[8]>2:
							return 'True'
						else: return 'True'
					elif obj[4]<=3:
						# {"feature": "Weather", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[15]>1.0:
								return 'True'
							elif obj[15]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[1]>0:
							# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[12]<=5:
								return 'False'
							elif obj[12]>5:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[10]<=1:
					# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[14]<=1.0:
						return 'False'
					elif obj[14]>1.0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]>0:
							return 'False'
						elif obj[7]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[17]>0:
				# {"feature": "Coupon", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Coffeehouse", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[14]<=3.0:
						# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[10]>0:
							# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=2:
									return 'True'
								elif obj[7]>2:
									return 'False'
								else: return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[10]<=0:
							# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[11]<=15:
								return 'True'
							elif obj[11]>15:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[14]>3.0:
						return 'False'
					else: return 'False'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>1:
			# {"feature": "Restaurantlessthan20", "instances": 55, "metric_value": 0.971, "depth": 3}
			if obj[15]<=3.0:
				# {"feature": "Age", "instances": 52, "metric_value": 0.9471, "depth": 4}
				if obj[7]<=6:
					# {"feature": "Bar", "instances": 50, "metric_value": 0.9248, "depth": 5}
					if obj[13]<=2.0:
						# {"feature": "Distance", "instances": 46, "metric_value": 0.9503, "depth": 6}
						if obj[18]>1:
							# {"feature": "Maritalstatus", "instances": 26, "metric_value": 0.8404, "depth": 7}
							if obj[8]>0:
								# {"feature": "Income", "instances": 19, "metric_value": 0.6292, "depth": 8}
								if obj[12]>3:
									# {"feature": "Children", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[14]>0.0:
											# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[4]>2:
												# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=2:
													return 'True'
												elif obj[10]>2:
													return 'False'
												else: return 'False'
											elif obj[4]<=2:
												return 'False'
											else: return 'False'
										elif obj[14]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[9]>0:
										return 'True'
									else: return 'True'
								elif obj[12]<=3:
									return 'True'
								else: return 'True'
							elif obj[8]<=0:
								# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[4]>1:
									# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[12]<=4:
										return 'True'
									elif obj[12]>4:
										return 'False'
									else: return 'False'
								elif obj[4]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[18]<=1:
							# {"feature": "Children", "instances": 20, "metric_value": 1.0, "depth": 7}
							if obj[9]>0:
								# {"feature": "Income", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[12]<=3:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[14]>0.0:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[16]>0.0:
											return 'True'
										elif obj[16]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[14]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[12]>3:
									return 'True'
								else: return 'True'
							elif obj[9]<=0:
								# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[10]<=2:
									# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[12]<=6:
										return 'False'
									elif obj[12]>6:
										return 'True'
									else: return 'True'
								elif obj[10]>2:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[13]>2.0:
						return 'True'
					else: return 'True'
				elif obj[7]>6:
					return 'False'
				else: return 'False'
			elif obj[15]>3.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[13]<=2.0:
			return 'True'
		elif obj[13]>2.0:
			return 'False'
		else: return 'False'
	else: return 'True'
