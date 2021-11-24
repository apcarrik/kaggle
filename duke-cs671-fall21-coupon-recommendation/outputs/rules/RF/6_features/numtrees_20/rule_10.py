def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[3]>1:
		# {"feature": "Education", "instances": 48, "metric_value": 0.995, "depth": 2}
		if obj[2]>0:
			# {"feature": "Passanger", "instances": 29, "metric_value": 0.9294, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Coupon", "instances": 20, "metric_value": 0.9341, "depth": 5}
					if obj[1]>0:
						# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[0]>0:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
