def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1.751715368871083:
		# {"feature": "Distance", "instances": 66, "metric_value": 0.994, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Coupon", "instances": 57, "metric_value": 0.9998, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Education", "instances": 39, "metric_value": 0.9612, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9294, "depth": 5}
					if obj[3]>0.0:
						return 'True'
					elif obj[3]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[3]<=2.0:
						return 'False'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>3:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Education", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>2:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1.751715368871083:
		# {"feature": "Education", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>3:
						return 'False'
					elif obj[0]<=3:
						return 'True'
					else: return 'True'
				elif obj[4]>1:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]>1.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
