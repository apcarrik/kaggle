def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 66, "metric_value": 0.9993, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 43, "metric_value": 0.9523, "depth": 3}
			if obj[3]<=10:
				# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.7496, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Education", "instances": 24, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[3]>10:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[4]>0.0:
							return 'False'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[5]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Distance", "instances": 23, "metric_value": 0.8865, "depth": 3}
			if obj[5]>1:
				# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 5}
					if obj[3]<=4:
						return 'False'
					elif obj[3]>4:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[4]>1.0:
							return 'False'
						elif obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[5]<=1:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[3]>8:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]<=8:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.4855, "depth": 2}
		if obj[3]<=10:
			return 'True'
		elif obj[3]>10:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[5]>1:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[5]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
