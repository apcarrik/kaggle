def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]>0:
		# {"feature": "Coffeehouse", "instances": 47, "metric_value": 0.9601, "depth": 2}
		if obj[7]<=3.0:
			# {"feature": "Occupation", "instances": 45, "metric_value": 0.9389, "depth": 3}
			if obj[5]<=14:
				# {"feature": "Age", "instances": 41, "metric_value": 0.965, "depth": 4}
				if obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Education", "instances": 24, "metric_value": 0.9799, "depth": 6}
						if obj[4]>1:
							# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 7}
							if obj[10]<=1:
								# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[6]<=1.0:
									return 'False'
								elif obj[6]>1.0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[10]>1:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]<=1.0:
											return 'False'
										elif obj[6]>1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=1:
							# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[10]<=2:
									# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[6]<=0.0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[9]>0:
												return 'False'
											elif obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]>0.0:
											return 'True'
										else: return 'True'
									elif obj[1]>1:
										return 'True'
									else: return 'True'
								elif obj[10]>2:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>1.0:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[6]<=0.0:
							return 'True'
						elif obj[6]>0.0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>14:
				return 'True'
			else: return 'True'
		elif obj[7]>3.0:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
