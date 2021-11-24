def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4744, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5889, "metric_value": 0.4618, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 5308, "metric_value": 0.4575, "depth": 3}
			if obj[2]>0:
				# {"feature": "Education", "instances": 5248, "metric_value": 0.4587, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Education", "instances": 60, "metric_value": 0.3183, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Education", "instances": 581, "metric_value": 0.4917, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 532, "metric_value": 0.4898, "depth": 4}
				if obj[2]<=7.648496240601504:
					return 'False'
				elif obj[2]>7.648496240601504:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 49, "metric_value": 0.4463, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 2258, "metric_value": 0.4882, "depth": 2}
		if obj[2]>2.015213346063521:
			# {"feature": "Education", "instances": 1795, "metric_value": 0.4911, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 1164, "metric_value": 0.4838, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 631, "metric_value": 0.4984, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=2.015213346063521:
			# {"feature": "Education", "instances": 463, "metric_value": 0.4395, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 410, "metric_value": 0.4354, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Distance", "instances": 53, "metric_value": 0.4135, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
