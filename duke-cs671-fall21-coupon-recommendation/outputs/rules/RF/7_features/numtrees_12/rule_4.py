def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[3]<=8:
		# {"feature": "Coupon", "instances": 57, "metric_value": 0.9819, "depth": 2}
		if obj[1]>1:
			# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.9103, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Distance", "instances": 32, "metric_value": 0.7579, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Education", "instances": 30, "metric_value": 0.65, "depth": 5}
					if obj[2]>0:
						# {"feature": "Passanger", "instances": 21, "metric_value": 0.7919, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			elif obj[4]>1.0:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[2]<=0:
								return 'False'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Passanger", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[0]>1:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=1:
						return 'False'
					elif obj[6]>1:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>8:
		# {"feature": "Education", "instances": 28, "metric_value": 0.6769, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Distance", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Passanger", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[0]>0:
						# {"feature": "Direction_same", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								return 'True'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
