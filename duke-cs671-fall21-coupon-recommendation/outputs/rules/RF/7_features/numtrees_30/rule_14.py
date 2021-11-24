def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Distance", "instances": 32, "metric_value": 0.9887, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Education", "instances": 30, "metric_value": 0.971, "depth": 3}
			if obj[2]>1:
				# {"feature": "Occupation", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[3]<=7:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[3]>7:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]>0:
						# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]<=0:
							return 'False'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[3]<=4:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[1]>1:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]>4:
						return 'True'
					else: return 'True'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	elif obj[4]>2.0:
		return 'True'
	else: return 'True'
