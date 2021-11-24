def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Coupon", "instances": 46, "metric_value": 0.9986, "depth": 2}
		if obj[1]>1:
			# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Distance", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[7]>1:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[3]>6:
							# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[4]>1.0:
									return 'True'
								elif obj[4]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[3]<=6:
							return 'False'
						else: return 'False'
					elif obj[7]<=1:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=10:
							return 'True'
						elif obj[3]>10:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>0.0:
									return 'False'
								elif obj[4]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>2.0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[2]<=1:
						return 'True'
					elif obj[2]>1:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=1:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[2]>1:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>1:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2:
									return 'True'
								else: return 'True'
							elif obj[4]>0.0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>0:
		return 'True'
	else: return 'True'
