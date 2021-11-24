def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Restaurant20to50", "instances": 81, "metric_value": 0.9867, "depth": 2}
		if obj[7]<=1.0:
			# {"feature": "Coupon", "instances": 55, "metric_value": 0.9998, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Bar", "instances": 37, "metric_value": 0.9569, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Time", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[4]>2:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=1:
											return 'False'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=2:
									return 'False'
								else: return 'False'
							elif obj[0]>2:
								return 'False'
							else: return 'False'
						elif obj[6]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[8]<=0:
							return 'True'
						elif obj[8]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=0.0:
					# {"feature": "Occupation", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[4]<=8:
						# {"feature": "Time", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1.0:
								return 'True'
							elif obj[6]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]>8:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]<=0:
								return 'False'
							elif obj[8]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Time", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[1]>1:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[4]<=7:
						# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[0]>1:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[9]>1:
									return 'True'
								elif obj[9]<=1:
									return 'False'
								else: return 'False'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					elif obj[4]>7:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>1.0:
			# {"feature": "Coupon", "instances": 26, "metric_value": 0.8404, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Bar", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[5]>-1.0:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 5}
					if obj[4]>2:
						# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[1]>1:
							# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[0]>1:
								# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[6]<=3.0:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>3.0:
									return 'True'
								else: return 'True'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]>0:
									# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=1:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							elif obj[6]>2.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=2:
						return 'True'
					else: return 'True'
				elif obj[5]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]>3:
		return 'True'
	else: return 'True'
