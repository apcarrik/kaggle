def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 5092, "metric_value": 0.4729, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 3688, "metric_value": 0.4601, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Education", "instances": 3346, "metric_value": 0.4554, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 3089, "metric_value": 0.459, "depth": 4}
				if obj[2]>1.9857345350584437:
					# {"feature": "Restaurant20to50", "instances": 2615, "metric_value": 0.4648, "depth": 5}
					if obj[3]<=3.0:
						return 'True'
					elif obj[3]>3.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=1.9857345350584437:
					# {"feature": "Restaurant20to50", "instances": 474, "metric_value": 0.4207, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 257, "metric_value": 0.3843, "depth": 4}
				if obj[2]<=12:
					# {"feature": "Restaurant20to50", "instances": 211, "metric_value": 0.4299, "depth": 5}
					if obj[3]>-1.0:
						return 'True'
					elif obj[3]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>12:
					# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.1556, "depth": 5}
					if obj[3]<=2.0:
						return 'True'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Education", "instances": 342, "metric_value": 0.4915, "depth": 3}
			if obj[1]<=4:
				# {"feature": "Occupation", "instances": 339, "metric_value": 0.4928, "depth": 4}
				if obj[2]<=7.551622418879056:
					# {"feature": "Restaurant20to50", "instances": 215, "metric_value": 0.4973, "depth": 5}
					if obj[3]<=3.0:
						return 'False'
					elif obj[3]>3.0:
						return 'False'
					else: return 'False'
				elif obj[2]>7.551622418879056:
					# {"feature": "Restaurant20to50", "instances": 124, "metric_value": 0.4759, "depth": 5}
					if obj[3]>-1.0:
						return 'False'
					elif obj[3]<=-1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 1404, "metric_value": 0.4818, "depth": 2}
		if obj[3]<=2.0:
			# {"feature": "Education", "instances": 1282, "metric_value": 0.4796, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 830, "metric_value": 0.4663, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Occupation", "instances": 698, "metric_value": 0.4766, "depth": 5}
					if obj[2]>2.089956186408986:
						return 'False'
					elif obj[2]<=2.089956186408986:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					# {"feature": "Occupation", "instances": 132, "metric_value": 0.4014, "depth": 5}
					if obj[2]<=7.962121212121212:
						return 'False'
					elif obj[2]>7.962121212121212:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Occupation", "instances": 452, "metric_value": 0.4882, "depth": 4}
				if obj[2]>1.7361629058784382:
					# {"feature": "Distance", "instances": 378, "metric_value": 0.497, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]<=1.7361629058784382:
					# {"feature": "Distance", "instances": 74, "metric_value": 0.4222, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>2.0:
			# {"feature": "Education", "instances": 122, "metric_value": 0.4413, "depth": 3}
			if obj[1]<=4:
				# {"feature": "Occupation", "instances": 115, "metric_value": 0.4555, "depth": 4}
				if obj[2]<=18:
					# {"feature": "Distance", "instances": 110, "metric_value": 0.4743, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]>18:
					return 'True'
				else: return 'True'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
