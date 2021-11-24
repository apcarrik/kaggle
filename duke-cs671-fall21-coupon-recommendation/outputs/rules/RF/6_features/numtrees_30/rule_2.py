def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Occupation", "instances": 26, "metric_value": 1.0, "depth": 2}
		if obj[3]<=17:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 3}
			if obj[1]>0:
				# {"feature": "Education", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]>17:
			return 'False'
		else: return 'False'
	elif obj[4]>1.0:
		# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[0]<=2:
			return 'True'
		elif obj[0]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
