def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[3]<=9:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[4]<=3.0:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							return 'True'
						else: return 'True'
					elif obj[7]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[4]>3.0:
				return 'False'
			else: return 'False'
		elif obj[3]>9:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=3:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>1.0:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>2:
		return 'False'
	else: return 'False'
