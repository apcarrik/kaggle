def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9465, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 64, "metric_value": 0.8571, "depth": 2}
		if obj[6]<=10:
			# {"feature": "Education", "instances": 44, "metric_value": 0.684, "depth": 3}
			if obj[5]<=1:
				# {"feature": "Age", "instances": 25, "metric_value": 0.2423, "depth": 4}
				if obj[4]<=5:
					return 'True'
				elif obj[4]>5:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>1:
				# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[8]<=3.0:
					# {"feature": "Bar", "instances": 16, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=0.0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[9]>1.0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=1:
									return 'False'
								elif obj[1]>1:
									return 'True'
								else: return 'True'
							elif obj[9]<=1.0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[7]>0.0:
						return 'True'
					else: return 'True'
				elif obj[8]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>10:
			# {"feature": "Time", "instances": 20, "metric_value": 1.0, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[8]>1.0:
								# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[4]>1:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]>1.0:
											return 'True'
										elif obj[9]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]<=1:
									return 'False'
								else: return 'False'
							elif obj[8]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[7]>0.0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]<=7:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[11]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[6]<=6:
			# {"feature": "Bar", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[7]<=0.0:
				return 'False'
			elif obj[7]>0.0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=2.0:
						return 'True'
					elif obj[8]>2.0:
						return 'False'
					else: return 'False'
				elif obj[4]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[6]>6:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[5]>0:
				return 'True'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
