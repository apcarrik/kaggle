def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Occupation", "instances": 48, "metric_value": 0.9987, "depth": 2}
		if obj[3]<=9:
			# {"feature": "Passanger", "instances": 34, "metric_value": 0.9597, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 26, "metric_value": 1.0, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[5]<=1:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>1:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[1]>1:
							return 'False'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[5]>1:
						return 'True'
					elif obj[5]<=1:
						# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]>2:
							return 'False'
						elif obj[1]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[3]>9:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[5]>1:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=1:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[4]>2.0:
		return 'True'
	else: return 'True'
