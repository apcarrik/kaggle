def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[1]>0:
		# {"feature": "Passanger", "instances": 70, "metric_value": 0.962, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 42, "metric_value": 0.9984, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.9881, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Occupation", "instances": 29, "metric_value": 0.9991, "depth": 5}
					if obj[3]>0:
						# {"feature": "Distance", "instances": 28, "metric_value": 0.9963, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[3]>4:
						return 'False'
					elif obj[3]<=4:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>2:
							return 'True'
						elif obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 28, "metric_value": 0.6769, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Occupation", "instances": 25, "metric_value": 0.4022, "depth": 4}
				if obj[3]>5:
					return 'True'
				elif obj[3]<=5:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[5]>1:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[3]<=12:
				return 'False'
			elif obj[3]>12:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=1.0:
					return 'False'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
