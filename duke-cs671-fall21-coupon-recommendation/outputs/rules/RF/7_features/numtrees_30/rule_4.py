def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]<=10:
		# {"feature": "Distance", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Coupon", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[1]>1:
				# {"feature": "Passanger", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	elif obj[3]>10:
		# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[4]<=2.0:
			return 'False'
		elif obj[4]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
