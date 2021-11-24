def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[3]<=7:
		# {"feature": "Coupon", "instances": 50, "metric_value": 0.9248, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 41, "metric_value": 0.7593, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 37, "metric_value": 0.8004, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Education", "instances": 34, "metric_value": 0.8338, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[4]<=2.0:
							return 'True'
						elif obj[4]>2.0:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[4]<=2.0:
							return 'True'
						elif obj[4]>2.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>7:
		# {"feature": "Passanger", "instances": 35, "metric_value": 0.971, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 31, "metric_value": 0.9932, "depth": 3}
			if obj[2]<=4:
				# {"feature": "Coupon", "instances": 30, "metric_value": 0.9871, "depth": 4}
				if obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9988, "depth": 5}
					if obj[4]<=3.0:
						# {"feature": "Distance", "instances": 24, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]>3.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=2:
						return 'False'
					elif obj[5]>2:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
