def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[3]>1:
		# {"feature": "Education", "instances": 73, "metric_value": 0.9988, "depth": 2}
		if obj[2]>0:
			# {"feature": "Coupon", "instances": 47, "metric_value": 0.9441, "depth": 3}
			if obj[1]>1:
				# {"feature": "Passanger", "instances": 28, "metric_value": 0.9963, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9829, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Distance", "instances": 25, "metric_value": 0.971, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[4]>2.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]<=1:
				# {"feature": "Passanger", "instances": 19, "metric_value": 0.7425, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[5]>1:
						# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[4]>-1.0:
							return 'False'
						elif obj[4]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=1:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.8905, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Passanger", "instances": 25, "metric_value": 0.8555, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 5}
					if obj[5]<=1:
						# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]>1:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[1]>1:
							return 'False'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[4]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[4]>1.0:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>1:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[4]<=1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
