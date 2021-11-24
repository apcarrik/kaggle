def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[6]<=3.0:
		# {"feature": "Time", "instances": 49, "metric_value": 0.9313, "depth": 2}
		if obj[1]>0:
			# {"feature": "Bar", "instances": 36, "metric_value": 0.8524, "depth": 3}
			if obj[5]>-1.0:
				# {"feature": "Coupon", "instances": 35, "metric_value": 0.8224, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Occupation", "instances": 21, "metric_value": 0.5917, "depth": 5}
					if obj[4]<=10:
						# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Passanger", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]>2:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[8]>2:
							return 'False'
						else: return 'False'
					elif obj[4]>10:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[4]<=10:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[0]>0:
							# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=2:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[4]>10:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=-1.0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]>1:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>1:
								return 'True'
							elif obj[4]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]>1:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[6]>3.0:
		return 'False'
	else: return 'False'
