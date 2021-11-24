def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]>0.0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[3]<=17:
			# {"feature": "Distance", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=3:
						return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>2:
				return 'False'
			else: return 'False'
		elif obj[3]>17:
			return 'False'
		else: return 'False'
	elif obj[4]<=0.0:
		return 'False'
	else: return 'False'
