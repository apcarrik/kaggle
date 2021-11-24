def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[2]>1.6794422404441178:
		# {"feature": "Education", "instances": 109, "metric_value": 0.9951, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 64, "metric_value": 0.9284, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 53, "metric_value": 0.9687, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Distance", "instances": 45, "metric_value": 0.9565, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Coupon", "instances": 40, "metric_value": 0.9097, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=0:
					return 'False'
				elif obj[0]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1.6794422404441178:
		# {"feature": "Distance", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
