def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[4]>0.0:
		# {"feature": "Occupation", "instances": 66, "metric_value": 0.9673, "depth": 2}
		if obj[3]<=12:
			# {"feature": "Education", "instances": 55, "metric_value": 0.9299, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 31, "metric_value": 0.8238, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 29, "metric_value": 0.8498, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Passanger", "instances": 22, "metric_value": 0.7732, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Distance", "instances": 24, "metric_value": 0.995, "depth": 4}
				if obj[5]<=1:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[5]>1:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[1]>0:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>12:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=0.0:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[3]>3:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]<=1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[5]>1:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>0:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=3:
			return 'False'
		else: return 'False'
	else: return 'False'
