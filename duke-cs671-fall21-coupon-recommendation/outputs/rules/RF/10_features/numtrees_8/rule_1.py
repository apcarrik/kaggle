def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9309, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 85, "metric_value": 0.9831, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Time", "instances": 43, "metric_value": 0.8542, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Coffeehouse", "instances": 30, "metric_value": 0.9481, "depth": 4}
				if obj[6]<=3.0:
					# {"feature": "Education", "instances": 27, "metric_value": 0.8767, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coupon", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[2]>0:
							# {"feature": "Distance", "instances": 16, "metric_value": 0.5436, "depth": 7}
							if obj[9]<=2:
								# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[5]>-1.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[5]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[9]>2:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=-1.0:
								return 'False'
							elif obj[5]>-1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]<=0:
						# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[8]>0:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								return 'False'
							else: return 'False'
						elif obj[8]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]>3.0:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[6]>0.0:
					return 'True'
				elif obj[6]<=0.0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[4]>6:
			# {"feature": "Bar", "instances": 42, "metric_value": 0.9852, "depth": 3}
			if obj[5]<=3.0:
				# {"feature": "Coupon", "instances": 39, "metric_value": 0.9957, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.9911, "depth": 5}
					if obj[7]>-1.0:
						# {"feature": "Education", "instances": 26, "metric_value": 0.9829, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.995, "depth": 7}
							if obj[6]<=3.0:
								# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 8}
								if obj[1]>0:
									# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9403, "depth": 10}
										if obj[8]>0:
											return 'True'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>3.0:
								return 'True'
							else: return 'True'
						elif obj[3]>3:
							return 'True'
						else: return 'True'
					elif obj[7]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[3]>1:
							# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=3.0:
								return 'True'
							elif obj[6]>3.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					elif obj[9]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[5]>3.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coffeehouse", "instances": 42, "metric_value": 0.7025, "depth": 2}
		if obj[6]>-1.0:
			# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.6098, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Education", "instances": 34, "metric_value": 0.4306, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Time", "instances": 26, "metric_value": 0.2352, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[4]>7:
							return 'True'
						elif obj[4]<=7:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>3:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[9]>1:
									return 'False'
								elif obj[9]<=1:
									return 'True'
								else: return 'True'
							elif obj[2]<=3:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>2:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[1]<=2:
							return 'True'
						elif obj[1]>2:
							# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=4:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]<=0.0:
				# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]<=-1.0:
			return 'False'
		else: return 'False'
	else: return 'True'
