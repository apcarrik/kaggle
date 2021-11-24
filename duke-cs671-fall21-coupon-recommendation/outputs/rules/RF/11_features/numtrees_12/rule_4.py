def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 56, "metric_value": 0.9917, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Coupon", "instances": 52, "metric_value": 0.9732, "depth": 3}
			if obj[2]>1:
				# {"feature": "Occupation", "instances": 35, "metric_value": 0.9994, "depth": 4}
				if obj[5]<=9:
					# {"feature": "Age", "instances": 24, "metric_value": 0.9544, "depth": 5}
					if obj[3]<=4:
						# {"feature": "Bar", "instances": 21, "metric_value": 0.9852, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[9]<=0:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[10]<=1:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8]<=2.0:
												return 'True'
											else: return 'True'
										elif obj[10]>1:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'True'
								else: return 'True'
							elif obj[9]>0:
								return 'True'
							else: return 'True'
						elif obj[6]<=0.0:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=2:
								return 'False'
							elif obj[10]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>4:
						return 'True'
					else: return 'True'
				elif obj[5]>9:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>1.0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Age", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]<=6:
						return 'True'
					elif obj[5]>6:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[4]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Education", "instances": 29, "metric_value": 0.6632, "depth": 2}
		if obj[4]>1:
			# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[2]>0:
					# {"feature": "Direction_same", "instances": 14, "metric_value": 0.7496, "depth": 5}
					if obj[9]<=0:
						# {"feature": "Age", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[3]<=3:
							return 'True'
						elif obj[3]>3:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[8]<=0.0:
								return 'False'
							elif obj[8]>0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
