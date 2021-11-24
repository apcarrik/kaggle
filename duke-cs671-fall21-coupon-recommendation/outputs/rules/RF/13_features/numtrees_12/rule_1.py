def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 53, "metric_value": 0.9874, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Age", "instances": 44, "metric_value": 1.0, "depth": 3}
			if obj[4]<=5:
				# {"feature": "Coffeehouse", "instances": 37, "metric_value": 0.9868, "depth": 4}
				if obj[9]<=3.0:
					# {"feature": "Coupon", "instances": 35, "metric_value": 0.971, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 25, "metric_value": 0.9988, "depth": 6}
						if obj[12]>1:
							# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 7}
							if obj[7]<=10:
								# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]>1.0:
												return 'True'
											elif obj[10]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									return 'False'
								else: return 'False'
							elif obj[7]>10:
								return 'True'
							else: return 'True'
						elif obj[12]<=1:
							# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=10:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[3]>0:
										return 'True'
									elif obj[3]<=0:
										# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[7]>10:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[8]<=1.0:
							return 'False'
						elif obj[8]>1.0:
							# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[1]>1:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]>1:
									return 'False'
								elif obj[7]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]>3.0:
					return 'True'
				else: return 'True'
			elif obj[4]>5:
				# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 32, "metric_value": 0.6962, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.8113, "depth": 3}
			if obj[7]<=10:
				# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[9]>1.0:
					return 'True'
				elif obj[9]<=1.0:
					# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>10:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>2:
						# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>0:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0.0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]<=2:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>2:
			return 'True'
		else: return 'True'
	else: return 'True'
