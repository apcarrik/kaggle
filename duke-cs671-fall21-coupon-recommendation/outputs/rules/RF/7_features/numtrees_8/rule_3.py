def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coupon", "instances": 115, "metric_value": 0.9986, "depth": 2}
		if obj[1]>1:
			# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.9766, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Direction_same", "instances": 67, "metric_value": 0.9921, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Occupation", "instances": 56, "metric_value": 0.9991, "depth": 5}
					if obj[3]<=10:
						# {"feature": "Distance", "instances": 45, "metric_value": 0.9825, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Passanger", "instances": 37, "metric_value": 0.9569, "depth": 7}
							if obj[0]>0:
								return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>10:
						# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[0]>1:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]>0:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[3]<=14:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[6]>1:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]>14:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[6]<=1:
						return 'True'
					elif obj[6]>1:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=9:
							return 'False'
						elif obj[3]>9:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.9569, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Passanger", "instances": 26, "metric_value": 0.7793, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 20, "metric_value": 0.8813, "depth": 5}
					if obj[3]>0:
						# {"feature": "Distance", "instances": 19, "metric_value": 0.8315, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[4]>1.0:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[6]>1:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]<=5:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]>5:
						return 'False'
					else: return 'False'
				elif obj[6]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[3]<=17:
			return 'True'
		elif obj[3]>17:
			return 'False'
		else: return 'False'
	else: return 'True'
