def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 53, "metric_value": 0.9997, "depth": 2}
		if obj[3]<=21:
			# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.9988, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Passanger", "instances": 29, "metric_value": 0.9784, "depth": 4}
				if obj[0]>0:
					# {"feature": "Coupon", "instances": 28, "metric_value": 0.9666, "depth": 5}
					if obj[1]>1:
						# {"feature": "Distance", "instances": 19, "metric_value": 0.8997, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[1]<=1:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				# {"feature": "Coupon", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]>1:
						return 'True'
					elif obj[5]<=1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]>21:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.8571, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Occupation", "instances": 27, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=14:
				# {"feature": "Coupon", "instances": 25, "metric_value": 0.9427, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 21, "metric_value": 0.8631, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Passanger", "instances": 19, "metric_value": 0.8997, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]>14:
				return 'True'
			else: return 'True'
		elif obj[4]>2.0:
			return 'True'
		else: return 'True'
	else: return 'True'
