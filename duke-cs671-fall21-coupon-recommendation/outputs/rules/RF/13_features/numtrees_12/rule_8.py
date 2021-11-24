def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9143, "depth": 1}
	if obj[6]>0:
		# {"feature": "Occupation", "instances": 55, "metric_value": 0.9883, "depth": 2}
		if obj[7]>5:
			# {"feature": "Coupon", "instances": 36, "metric_value": 0.9978, "depth": 3}
			if obj[2]>1:
				# {"feature": "Direction_same", "instances": 27, "metric_value": 0.9751, "depth": 4}
				if obj[11]<=0:
					# {"feature": "Age", "instances": 24, "metric_value": 0.995, "depth": 5}
					if obj[4]<=6:
						# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Bar", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=0.0:
								# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[5]<=0:
												return 'False'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[10]>2.0:
										return 'False'
									else: return 'False'
								elif obj[9]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[8]>0.0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]>1:
										return 'False'
									elif obj[0]<=1:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=3.0:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[8]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>6:
						return 'False'
					else: return 'False'
				elif obj[11]>0:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[7]<=5:
			# {"feature": "Age", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[4]>1:
				# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[9]>1.0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				elif obj[9]<=1.0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[12]<=1:
						return 'False'
					elif obj[12]>1:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]<=0.0:
							return 'True'
						elif obj[8]>0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[6]<=0:
		# {"feature": "Time", "instances": 30, "metric_value": 0.5665, "depth": 2}
		if obj[1]>1:
			# {"feature": "Age", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[4]>0:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[12]<=2:
					# {"feature": "Bar", "instances": 16, "metric_value": 0.5436, "depth": 5}
					if obj[8]>0.0:
						return 'True'
					elif obj[8]<=0.0:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[2]>0:
							# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[9]>0.0:
								return 'True'
							elif obj[9]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]>2:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
