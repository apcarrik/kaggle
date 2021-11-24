def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9762, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 98, "metric_value": 0.9313, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.9891, "depth": 3}
			if obj[3]>0.0:
				# {"feature": "Occupation", "instances": 55, "metric_value": 0.9806, "depth": 4}
				if obj[2]>3:
					# {"feature": "Distance", "instances": 45, "metric_value": 0.9968, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=3:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 41, "metric_value": 0.7593, "depth": 3}
			if obj[2]<=10:
				# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.5788, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Distance", "instances": 20, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[3]>1.0:
					return 'True'
				else: return 'True'
			elif obj[2]>10:
				# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[3]>2.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9576, "depth": 2}
		if obj[3]<=1.0:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=14:
				# {"feature": "Education", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[2]>14:
				return 'True'
			else: return 'True'
		elif obj[3]>1.0:
			# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[2]>2:
					return 'True'
				elif obj[2]<=2:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
