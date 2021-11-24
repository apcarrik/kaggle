def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Distance", "instances": 46, "metric_value": 0.9945, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Occupation", "instances": 43, "metric_value": 0.9996, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.992, "depth": 4}
				if obj[3]<=3.0:
					# {"feature": "Coupon", "instances": 36, "metric_value": 0.9978, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]>3.0:
					return 'False'
				else: return 'False'
			elif obj[2]>12:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
