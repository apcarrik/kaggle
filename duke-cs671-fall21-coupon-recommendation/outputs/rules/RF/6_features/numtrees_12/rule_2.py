def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Occupation", "instances": 57, "metric_value": 0.998, "depth": 2}
		if obj[3]<=9:
			# {"feature": "Coupon", "instances": 45, "metric_value": 0.9911, "depth": 3}
			if obj[1]>1:
				# {"feature": "Passanger", "instances": 33, "metric_value": 0.9457, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 31, "metric_value": 0.9072, "depth": 5}
					if obj[5]<=1:
						# {"feature": "Education", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>1:
						# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[2]<=1:
							return 'True'
						elif obj[2]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[5]<=2:
						return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=2:
						return 'True'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[3]>9:
			# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[5]>1:
				return 'False'
			elif obj[5]<=1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>1:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[4]>1.0:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.8631, "depth": 2}
		if obj[3]>5:
			# {"feature": "Coupon", "instances": 21, "metric_value": 0.7025, "depth": 3}
			if obj[1]>0:
				# {"feature": "Passanger", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]<=5:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]>2:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
