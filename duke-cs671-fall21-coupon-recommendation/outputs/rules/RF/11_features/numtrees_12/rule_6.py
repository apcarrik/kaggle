def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Bar", "instances": 62, "metric_value": 0.9629, "depth": 2}
		if obj[6]<=3.0:
			# {"feature": "Age", "instances": 59, "metric_value": 0.9393, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Coupon", "instances": 34, "metric_value": 0.7871, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=2.0:
						# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 6}
						if obj[5]>1:
							# {"feature": "Distance", "instances": 19, "metric_value": 0.7425, "depth": 7}
							if obj[10]<=2:
								# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.8366, "depth": 8}
								if obj[8]>1.0:
									# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[1]>2:
										# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=2:
										return 'False'
									else: return 'False'
								elif obj[8]<=1.0:
									# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[1]>1:
										# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[4]>1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									elif obj[1]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[10]>2:
								return 'False'
							else: return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[7]>2.0:
						# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]>12:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[8]>1.0:
								return 'True'
							elif obj[8]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[5]<=12:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[3]>3:
				# {"feature": "Occupation", "instances": 25, "metric_value": 0.9988, "depth": 4}
				if obj[5]<=7:
					# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[10]<=1:
						# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[4]<=1:
								# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=2.0:
										return 'True'
									elif obj[7]>2.0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]>1:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[10]>1:
						# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[4]<=2:
							return 'False'
						elif obj[4]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]>7:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[10]>1:
							return 'True'
						elif obj[10]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>3.0:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[2]>1:
			# {"feature": "Time", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[1]>2:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[5]>4:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[7]<=2.0:
						return 'True'
					elif obj[7]>2.0:
						return 'False'
					else: return 'False'
				elif obj[5]<=4:
					return 'False'
				else: return 'False'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[6]<=0.0:
				return 'False'
			elif obj[6]>0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
