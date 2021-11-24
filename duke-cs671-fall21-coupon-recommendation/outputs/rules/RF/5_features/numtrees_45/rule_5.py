def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[2]>4:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]<=2.0:
						return 'True'
					elif obj[3]>2.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>-1.0:
						return 'False'
					elif obj[3]<=-1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=4:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
