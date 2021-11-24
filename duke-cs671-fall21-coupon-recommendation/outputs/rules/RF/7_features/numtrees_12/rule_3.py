def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 66, "metric_value": 0.976, "depth": 2}
		if obj[3]<=10:
			# {"feature": "Coupon", "instances": 44, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				# {"feature": "Education", "instances": 30, "metric_value": 0.971, "depth": 4}
				if obj[2]>0:
					# {"feature": "Distance", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 1.0, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]>2:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>10:
			# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.7732, "depth": 3}
			if obj[4]>-1.0:
				# {"feature": "Education", "instances": 21, "metric_value": 0.7025, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 14, "metric_value": 0.3712, "depth": 5}
					if obj[6]<=2:
						return 'False'
					elif obj[6]>2:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[6]<=1:
						# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]>2:
								return 'False'
							elif obj[1]<=2:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					elif obj[6]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=-1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.4855, "depth": 2}
		if obj[6]>1:
			return 'True'
		elif obj[6]<=1:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[3]>5:
				return 'True'
			elif obj[3]<=5:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=1.0:
					return 'False'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'True'
