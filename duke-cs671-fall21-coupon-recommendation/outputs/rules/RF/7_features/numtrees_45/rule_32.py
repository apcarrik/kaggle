def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[3]>1:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]>1.0:
								return 'True'
							elif obj[4]<=1.0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>4:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=4:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
