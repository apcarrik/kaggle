def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[3]>6:
		# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.8767, "depth": 2}
		if obj[4]>1.0:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[4]<=1.0:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2]<=2:
					return 'False'
				elif obj[2]>2:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>1:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=4:
							return 'False'
						else: return 'False'
					elif obj[5]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>3:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1:
						return 'True'
					elif obj[5]>1:
						return 'False'
					else: return 'False'
				elif obj[1]<=3:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=6:
		# {"feature": "Distance", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[5]>1:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[0]>1:
				# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=1:
							return 'True'
						elif obj[2]>1:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>3:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[1]<=3:
						return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[5]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
