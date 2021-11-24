def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4722, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 5903, "metric_value": 0.4599, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 5355, "metric_value": 0.4555, "depth": 3}
			if obj[2]>0:
				# {"feature": "Education", "instances": 5295, "metric_value": 0.457, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Education", "instances": 60, "metric_value": 0.2773, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Education", "instances": 548, "metric_value": 0.4922, "depth": 3}
			if obj[1]<=4:
				# {"feature": "Occupation", "instances": 545, "metric_value": 0.4933, "depth": 4}
				if obj[2]<=7.609174311926606:
					return 'False'
				elif obj[2]>7.609174311926606:
					return 'False'
				else: return 'False'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 2244, "metric_value": 0.4844, "depth": 2}
		if obj[1]>0:
			# {"feature": "Distance", "instances": 1454, "metric_value": 0.4759, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 1199, "metric_value": 0.4795, "depth": 4}
				if obj[2]<=18.865081162029256:
					return 'False'
				elif obj[2]>18.865081162029256:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				# {"feature": "Occupation", "instances": 255, "metric_value": 0.4511, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 790, "metric_value": 0.4907, "depth": 3}
			if obj[2]>1.661424080504549:
				# {"feature": "Distance", "instances": 670, "metric_value": 0.4996, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=1.661424080504549:
				# {"feature": "Distance", "instances": 120, "metric_value": 0.4305, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
