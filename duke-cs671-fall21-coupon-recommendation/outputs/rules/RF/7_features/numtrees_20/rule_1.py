def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[3]>1:
		# {"feature": "Distance", "instances": 47, "metric_value": 0.9971, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Education", "instances": 41, "metric_value": 0.9789, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 31, "metric_value": 0.9992, "depth": 4}
				if obj[1]>1:
					# {"feature": "Direction_same", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[4]<=3.0:
							# {"feature": "Passanger", "instances": 16, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]>3.0:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[0]>0:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[4]>0.0:
								return 'True'
							elif obj[4]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]<=1.0:
						return 'False'
					elif obj[4]>1.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=0:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]>1.0:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
