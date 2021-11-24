def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[8]>0.0:
		# {"feature": "Time", "instances": 64, "metric_value": 0.896, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 57, "metric_value": 0.9348, "depth": 3}
			if obj[6]>4:
				# {"feature": "Direction_same", "instances": 40, "metric_value": 0.8485, "depth": 4}
				if obj[10]<=0:
					# {"feature": "Age", "instances": 28, "metric_value": 0.6769, "depth": 5}
					if obj[4]>1:
						# {"feature": "Distance", "instances": 18, "metric_value": 0.8524, "depth": 6}
						if obj[11]<=2:
							# {"feature": "Coupon", "instances": 16, "metric_value": 0.6962, "depth": 7}
							if obj[2]>1:
								# {"feature": "Education", "instances": 13, "metric_value": 0.3912, "depth": 8}
								if obj[5]<=2:
									return 'True'
								elif obj[5]>2:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=2:
										return 'True'
									elif obj[0]>2:
										# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>0.0:
											return 'False'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[2]<=1:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]>1:
									return 'False'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[11]>2:
							return 'False'
						else: return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[10]>0:
					# {"feature": "Coupon", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=1:
									# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[0]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								elif obj[11]>1:
									return 'True'
								else: return 'True'
							elif obj[9]>1.0:
								return 'True'
							else: return 'True'
						elif obj[4]>6:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]<=4:
				# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[2]>1:
						# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[5]<=2:
							# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3]>0:
								# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[10]<=0:
											return 'False'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										return 'True'
									else: return 'True'
								elif obj[4]>0:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[7]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[8]<=0.0:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[5]>0:
				# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[6]>4:
						return 'False'
					elif obj[6]<=4:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					return 'True'
				else: return 'True'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
